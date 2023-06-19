//
//  CharacterView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/19.
//

import SwiftUI

enum CharacterViewKind {
    case generateCharacter
    case generatingCharacter
    case registerCharacter
    case registeringCharacter
}

struct CharacterView: View {
    @ObservedObject private(set) var presenter = Presenter()
    
    var body: some View {
        switch presenter.viewState.viewKind {
        case .generateCharacter:
            GenerateCharacterView(presenter: presenter)
        case .generatingCharacter:
            ProgressView()
        case .registerCharacter:
            RegisterCharacterView(presenter: presenter)
        case .registeringCharacter:
            ProgressView()
        }
    }
}

struct CharacterView_Previews: PreviewProvider {
    static var previews: some View {
        CharacterView()
    }
}
