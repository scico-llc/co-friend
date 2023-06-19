//
//  GenerateCharacterPresenter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import SwiftUI

extension GenerateCharacterView {
    struct ViewState {
        fileprivate(set) var animalTypeText: String = ""
        fileprivate(set) var loading: Bool = false
    }
    
    final class Presenter: ObservableObject {
        @Published private(set) var viewState = ViewState()
        
        func onAnimalTypeTextChange(_ text: String) {
            viewState.animalTypeText = text
        }
        
        func onTapGenerateImageButton() {
            viewState.loading = true
            Task {
                do {
                    let uuid = UUID()
                    let parameters = GetCharactersImageParameters(walletAddress: Constants.walletAddress,
                                                                  animalId: uuid.uuidString,
                                                                  animalType: viewState.animalTypeText)
                    let request = RequestGetCharactersImage(parameters: parameters)
                    let response = try await APIClient.request(request)
                    viewState.loading = false
                    print(response.imageUrls)
                } catch let error {
                    print("error occurred:", error)
                }
            }
        }
    }
}

