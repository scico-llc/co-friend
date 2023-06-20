//
//  ChatViewPresenter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Foundation
import FirebaseFirestoreSwift

extension ChatView {
    @MainActor struct ViewState {
        fileprivate(set) var messageInputText: String = ""
        fileprivate(set) var chatSending: Bool = false
        fileprivate var chat: Chat = .init(id: "0", history: [], name: "", type: "")
        
        var chatMessages: [ChatMessage] {
            // role が system のメッセージは取り除く
            let history = chat.history.filter { $0.role != "system" }
            // role が assistant のメッセージにはURLを付与する
            let messages: [ChatMessage] = history.map { message in
                let chatMessage: ChatMessage
                if message.role == "assistant" {
                    chatMessage = ChatMessage(imageUrl: animalImageUrl, role: chat.name, content: message.content)
                } else {
                    chatMessage = ChatMessage(imageUrl: nil, role: message.role, content: message.content)
                }
                return chatMessage
            }
            return messages
        }
        
        // 内部状態
        fileprivate var animalId: String?
        fileprivate var animalImageUrl: String?
    }
    
    @MainActor final class Presenter: ObservableObject {
        @Published private(set) var viewState = ViewState()
        
        func onAppeare() {
            viewState.animalId = UserDefaultsClient.animalId
            viewState.animalImageUrl = UserDefaultsClient.animalImageUrl
            fetchChat()
        }
        
        func onMessageInputTextChange(_ text: String) {
            viewState.messageInputText = text
        }
        
        func onTapSendMessageButton() {
            guard let animalId = viewState.animalId else { return }
            
            viewState.chatSending = true
            Task {
                do {
                    let parameters = PostChatParameters(animalId: animalId, message: viewState.messageInputText)
                    let request = RequestPostChat(parameters: parameters)
                    let response = try await APIClient.request(request)
                    print("response message:", response.message)
                    viewState.messageInputText = ""
                    viewState.chatSending = false
                    fetchChat()
                } catch {
                    print("onTapSendMessageButton error:", error)
                    viewState.chatSending = false
                }
            }
        }
        
        private func fetchChat() {
            guard let animalId = viewState.animalId else {
                 viewState.chat = Chat(id: "", history: [Message(role: "System", content: "右上の ＋ マークから友達キャラクターを登録しましょう！")], name: "", type: "")
                 return }
            
            Task {
                do {
                    let chat = try await FirestoreClient.shared.db.collection("characters").document(animalId).getDocument(as: Chat.self)
                    viewState.chat = chat
                } catch {
                    print("fetchChat error:", error)
                }
            }
        }
    }
}

