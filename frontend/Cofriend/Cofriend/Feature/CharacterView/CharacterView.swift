//
//  CharacterView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/19.
//

import SwiftUI

enum CharacterViewKind {
    case generate
    case generating
    case register
    case registering
    case complete
}

struct CharacterView: View {
    @ObservedObject private(set) var presenter = Presenter()
    
    var body: some View {
        switch presenter.viewState.viewKind {
        case .generate:
            GenerateCharacterView(presenter: presenter)
        case .generating:
            ProgressView()
        case .register:
            RegisterCharacterView(presenter: presenter)
        case .registering:
            ProgressView()
        case .complete:
            RegisterCompleteView()
        }
    }
}

struct CharacterView_Previews: PreviewProvider {
    static var previews: some View {
        CharacterView()
    }
}
