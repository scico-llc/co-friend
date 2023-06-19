//
//  GenerateCharacter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import SwiftUI

struct GenerateCharacterView: View {
    
    @ObservedObject private(set) var presenter: CharacterView.Presenter
        
    var body: some View {
        GenerateCharacterViewContent(presenter: presenter)
    }
}

struct GenerateCharacterViewContent: View {
    let presenter: CharacterView.Presenter
    
    var body: some View {
        VStack {
            Spacer().frame(height: 32)
            VStack {
                Text("キャラクター種類")
                TextField("ネコ", text: .init(get: {
                    presenter.viewState.animalTypeText
                }, set: { text in
                    presenter.onAnimalTypeTextChange(text)
                }))
            }.padding(.horizontal, 32)
            Spacer()
            Button(action: {
                presenter.onTapGenerateImageButton()
            }, label: {
                Text("作成")
            })
            Spacer().frame(height: 32)
        }
    }
}

struct GenerateCharacterImage_Previews: PreviewProvider {
    static var previews: some View {
        GenerateCharacterView(presenter: CharacterView.Presenter())
    }
}
