//
//  RegisterCharacterView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/17.
//

import SwiftUI

struct RegisterCharacterView: View {
    @ObservedObject private(set) var presenter: CharacterView.Presenter
    
    var body: some View {
        ScrollView {
            RegisterCharacterViewContent(presenter: presenter)
        }
        
    }
}

struct RegisterCharacterViewContent: View {
    let presenter: CharacterView.Presenter
    @State var selectedImageIndex: Int = -1
    
    var body: some View {
        VStack(alignment: .center, spacing: 0) {
            Spacer().frame(height: 32)
            VStack(alignment: .leading, spacing: 32) {
                Text("オリジナルのキャラクターを3体生み出しました！")
                    .font(.subheadline)
                Text("Step1 友達にしたいキャラクターを選びましょう！")
                    .font(.subheadline)
                
                VStack(alignment: .center) {
                    HStack {
                        
                        ForEach(0 ..< presenter.viewState.animalImageUrls.count, id: \.self) { index in
                            let imageUrl = presenter.viewState.animalImageUrls[index]
                            Button(action: {
                                presenter.onTapAnimalImage(imageUrl)
                                selectedImageIndex = index
                            }, label: {
                                AsyncImage(url: URL(string: imageUrl)) { image in
                                    image
                                        .resizable()
                                        .aspectRatio(contentMode: .fit)
                                        .opacity(selectedImageIndex == index || selectedImageIndex == -1 ? 1.0 : 0.4)
                                } placeholder: {
                                    ProgressView()
                                }
                            })
                        }
                    }.frame(minHeight: 100)
                }
                                    
                Text("Step2 名前を付けよう！")
                    .font(.subheadline)
                TextField("たろう", text: .init(get: {
                    presenter.viewState.animalName
                }, set: { text in
                    presenter.onAnimalNameTextChange(text)
                }))
                .frame(minHeight: 55)
                .padding(.horizontal, 16)
                .overlay(RoundedRectangle(cornerRadius: 8)
                    .stroke(Color.gray))
                .padding(.bottom, 12)
            }
            Spacer()
            FilledButton(text: "確定", action: {
                presenter.onTapRegisterButton()
            })
            Spacer().frame(height: 32)
        }
        .padding(.horizontal, 24)
    }
}

struct GenerateFriendView_Previews: PreviewProvider {
    static var previews: some View {
        RegisterCharacterView(presenter: CharacterView.Presenter())
    }
}
