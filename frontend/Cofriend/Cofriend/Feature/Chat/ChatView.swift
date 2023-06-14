//
//  ChatView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/14.
//

import SwiftUI

struct ChatView: View {
    let message1 = Message(autherName: "Person",
                          autherImageName: "person",
                          text: "Sampleだよ")
    let message2 = Message(autherName: "Person",
                          autherImageName: "person",
                          text: "SampleだよSampleだよSampleだよSampleだよSampleだよ")
    
    var body: some View {
        VStack(spacing: 16) {
            MessageView(message: message1)
            MessageView(message: message2)
            MessageView(message: message1)
        }
        .padding(.horizontal, 16)
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

struct Message {
    let autherName: String
    let autherImageName: String
    let text: String
}

struct ChatView_Previews: PreviewProvider {
    static var previews: some View {
        ChatView()
    }
}
