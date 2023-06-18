//
//  GenerateCharacter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import SwiftUI

struct GenerateCharacterView: View {
    let presenter: Presenter
    
    var body: some View {
        ZStack {
            GenerateCharacterViewContent(presenter: presenter)
        }
        .onAppear {
            presenter.onAppear()
        }
    }
}

struct GenerateCharacterViewContent: View {
    let presenter: GenerateCharacterView.Presenter
    
    var body: some View {
        VStack {
            Spacer().frame(height: 32)
            VStack {
                Text("キャラクター種類")
                TextField("ネコ", text: presenter.viewState.$characterKindText)
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
        let presenter = GenerateCharacterView.Presenter()
        GenerateCharacterView(presenter: presenter)
    }
}
