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
        fileprivate(set) var chat: Chat = .init(id: "0", history: [], name: "", type: "")
    }
    
    @MainActor final class Presenter: ObservableObject {
        @Published private(set) var viewState = ViewState()
        // 内部状態
        private var animalId: String?
        private var animalImageUrl: String?
        
        func onAppeare() {
            animalId = UserDefaultsClient.animalId
            animalImageUrl = UserDefaultsClient.animalImageUrl
            fetchChat()
        }
        
        func onMessageInputTextChange(_ text: String) {
            viewState.messageInputText = text
        }
        
        func onTapSendMessageButton() {
            guard let animalId = animalId else { return }
//            let animalId = "xxxxxxxxxxxx123"
            
            Task {
                do {
                    let parameters = PostChatParameters(animalId: animalId, message: viewState.messageInputText)
                    let request = RequestPostChat(parameters: parameters)
                    let response = try await APIClient.request(request)
                    print("response message:", response.message)
                    viewState.messageInputText = ""
                    fetchChat()
                } catch {
                    print("onTapSendMessageButton error:", error)
                }
            }
        }
        
        private func fetchChat() {
             guard let animalId = animalId else {
                 viewState.chat = Chat(id: "", history: [Message(role: "System", content: "右上の ＋ マークから友達キャラクターを登録しましょう！")], name: "", type: "")
                 return }
//            let animalId = "xxxxxxxxxxxx123"
            
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

