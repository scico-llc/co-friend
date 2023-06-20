//
//  ChatView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/14.
//

import SwiftUI

struct ChatView: View {
    @ObservedObject private(set) var presenter = Presenter()
    
    var body: some View {
        let content = ChatContetView(presenter: presenter)
        
        return NavigationStack {
            content
                .onAppear {
                    presenter.onAppeare()
                }
        }.navigationBarTitle("CO-friend", displayMode: .automatic)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    NavigationLink(destination: CharacterView()) {
                        Image(systemName: "plus.circle")
                    }
                }
            }
    }
}

struct ChatContetView: View {
    @ObservedObject private(set) var presenter: ChatView.Presenter
    
    var body: some View {
        VStack(spacing: 0) {
            List {
                ForEach(0 ..< presenter.viewState.chat.history.count, id: \.self) { index in
                    let message = presenter.viewState.chat.history[index]
                    MessageView(message: message)
                }.listRowSeparator(.hidden)
            }.listStyle(.plain)
                .padding(.horizontal, 12)
            HStack(spacing: 8) {
                TextField("Message", text: .init(get: {
                    presenter.viewState.messageInputText
                }, set: { text in
                    presenter.onMessageInputTextChange(text)
                }))
                .textFieldStyle(.roundedBorder)
                Button(action: {
                    presenter.onTapSendMessageButton()
                }, label: {
                    Image(systemName: "arrow.up.circle.fill")
                        .resizable()
                        .frame(width: 32, height: 32)
                })
            }.padding(18)
        }
    }
}

struct MessageView: View {
    let message: Message
    var body: some View {
        HStack(alignment: .center) {
            Image(systemName: "person")
                .resizable()
                .frame(width: 24, height: 24)
                .cornerRadius(10)
            VStack(alignment: .leading) {
                Text(message.role)
                    .font(.subheadline)
                    .foregroundColor(.gray)
                Text(message.content)
                    .font(.body)
            }
            Spacer()
        }
    }
}

struct ChatView_Previews: PreviewProvider {
    static var previews: some View {
        ChatView()
    }
}
