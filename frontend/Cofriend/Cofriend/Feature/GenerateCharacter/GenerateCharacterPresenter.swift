//
//  GenerateCharacterPresenter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import SwiftUI

extension GenerateCharacterView {
    final class ViewState: ObservableObject {
        @State var characterKindText: String = ""
        @State var loading: Bool = false
    }
    
    struct Presenter {
        let viewState = ViewState()
        
        func onAppear() {
            print("onAppear")
        }
        
        func onTapGenerateImageButton() {
            print("onTapGenerateImageButton")
        }
    }
}
