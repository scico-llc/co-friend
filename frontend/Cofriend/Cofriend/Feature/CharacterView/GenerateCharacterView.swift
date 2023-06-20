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
            VStack(alignment: .leading) {
                Text("キャラクターの種類")
                    .font(.subheadline)
                TextField("ネコ", text: .init(get: {
                    presenter.viewState.animalTypeText
                }, set: { text in
                    presenter.onAnimalTypeTextChange(text)
                }))
                .frame(minHeight: 55)
                .padding(.horizontal, 16)
                .overlay(RoundedRectangle(cornerRadius: 8)
                    .stroke(Color.gray))
                
            }.padding(.horizontal, 32)
            Spacer()
            
            FilledButton(text: "キャラクターを生み出す") {
                presenter.onTapGenerateImageButton()
            }.padding(.horizontal, 32)
            Spacer().frame(height: 32)
        }
    }
}

struct GenerateCharacterImage_Previews: PreviewProvider {
    static var previews: some View {
        GenerateCharacterView(presenter: CharacterView.Presenter())
    }
}
