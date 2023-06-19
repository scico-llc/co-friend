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
        RegisterCharacterViewContent(presenter: presenter)
    }
}

struct RegisterCharacterViewContent: View {
    let presenter: CharacterView.Presenter
    
    var body: some View {
        VStack(alignment: .center, spacing: 0) {
            Spacer().frame(height: 32)
            VStack(alignment: .leading, spacing: 32) {
                Text("Step1 友達にしたいキャラクターを選ぼう！")
                
                HStack {
                                    
                    ForEach(presenter.viewState.animalImageUrls, id: \.self) { imageUrl in
                        Button(action: {
                            presenter.onTapAnimalImage(imageUrl)
                        }, label: {
                            AsyncImage(url: URL(string: imageUrl)) { image in
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
                TextField("名前", text: .init(get: {
                    presenter.viewState.animalName
                }, set: { text in
                    presenter.onAnimalNameTextChange(text)
                }))
                .textFieldStyle(.roundedBorder)
                .padding(.bottom, 12)
            }
            Spacer()
            Button(action: {
                presenter.onTapRegisterButton()
            }, label: {
                Text("確定")
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
