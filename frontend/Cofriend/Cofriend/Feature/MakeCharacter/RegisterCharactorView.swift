//
//  RegisterCharacterView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/17.
//

import SwiftUI

struct RegisterCharacterView: View {
    var body: some View {
        RegisterCharacterViewContent()
    }
}

struct RegisterCharacterViewContent: View {
    @State private var name = ""
    @State private var images = ["https://img.freepik.com/free-photo/cute-kitten-staring-out-the-window-playful-curiosity-generative-ai_188544-12520.jpg", "https://img.freepik.com/premium-photo/shiba-inu-dog-sitting-and-panting-cut-out_191971-5628.jpg"]
    
    var body: some View {
        VStack(alignment: .center, spacing: 0) {
            Spacer().frame(height: 32)
            VStack(alignment: .leading, spacing: 32) {
                Text("Step1 友達にしたいキャラクターを選ぼう！")
                
                HStack {
                                    
                    ForEach(images, id: \.self) { image in
                        Button(action: {
                        }, label: {
                            AsyncImage(url: URL(string: image)) { image in
                                image
                                    .resizable()
                                    .aspectRatio(contentMode: .fit)
                            } placeholder: {
                                ProgressView()
                            }
                        })
                    }
                }
                                    
                Text("Step2 名前を付けよう！")
                    .font(.subheadline)
                TextField("Input friend name",
                            text: $name)
                    .textFieldStyle(.roundedBorder)
                    .padding(.bottom, 12)
            }
            Spacer()
            Button(action: {
                print("tapped")
            }, label: {
                Text("確定")
            })
            Spacer().frame(height: 32)
        }
        .padding(.horizontal, 24)
    }
}

struct MakeFriendView_Previews: PreviewProvider {
    static var previews: some View {
        RegisterCharacterView()
    }
}
