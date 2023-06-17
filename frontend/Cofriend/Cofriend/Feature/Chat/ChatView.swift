//
//  ChatView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/14.
//

import SwiftUI

struct ChatView: View {
    let messages: [Message] = (0..<10).map { i in
        Message(id: i,
                autherName: "Person",
                autherImageName: "person",
                text: "Sampleだよ")
    }
    @State private var input = ""
    
    var body: some View {
        VStack(spacing: 0) {
            List {
                ForEach(messages) { message in
                    MessageView(message: message)
                }.listRowSeparator(.hidden)
            }.listStyle(.plain)
                .padding(.horizontal, 12)
            HStack(spacing: 8) {
                TextField("Message",
                          text: $input)
                .textFieldStyle(.roundedBorder)
                Button(action: {
                    print("tapped")
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
            Image(systemName: message.autherImageName)
                .resizable()
                .frame(width: 24, height: 24)
                .cornerRadius(10)
            VStack(alignment: .leading) {
                Text(message.autherName)
                    .font(.subheadline)
                    .foregroundColor(.gray)
                Text(message.text)
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
