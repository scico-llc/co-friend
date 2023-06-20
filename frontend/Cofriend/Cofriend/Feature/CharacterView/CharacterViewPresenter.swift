//
//  CharacterViewPresenter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/19.
//

import Foundation

extension CharacterView {
    @MainActor struct ViewState {
        fileprivate(set) var viewKind: CharacterViewKind = .generate
        
        // GenerateCharacter画面で利用
        fileprivate(set) var animalTypeText: String = ""
        fileprivate(set) var animalId: String = ""
        fileprivate(set) var animalImageUrls: [String] = []
        
        // RegisterCharacter画面で利用
        fileprivate(set) var animalName: String = ""
        fileprivate(set) var selectedAnimalImageUrl: String = ""
    }
    
    @MainActor final class Presenter: ObservableObject {
        @Published private(set) var viewState = ViewState()
    }
}

// - MARK: GenerateCharacter

extension CharacterView.Presenter {
    func onAnimalTypeTextChange(_ text: String) {
        viewState.animalTypeText = text
    }
    
    func onTapGenerateImageButton() {
        viewState.viewKind = .generating
        Task {
            do {
                let animalId = UUID().uuidString
                let parameters = PostCharactersImageParameters(walletAddress: Constants.walletAddress,
                                                               animalId: animalId,
                                                               animalType: viewState.animalTypeText)
                let request = RequestPostCharactersImage(parameters: parameters)
                let response = try await APIClient.request(request)

                // Mock
                // let animalId = "1234"
                // let response = PostCharactersImageResponse(imageUrls: ["https://storage.googleapis.com/co-friend-dev.appspot.com/1234/0.png",
                //                                                        "https://storage.googleapis.com/co-friend-dev.appspot.com/1234/1.png",
                //                                                        "https://storage.googleapis.com/co-friend-dev.appspot.com/1234/2.png"])

                viewState.animalId = animalId
                viewState.animalImageUrls = response.imageUrls
                viewState.viewKind = .register
            } catch let error {
                print("error occurred:", error)
                viewState.viewKind = .generate
            }
        }
    }
}


// - MARK: RegisterCharacter

extension CharacterView.Presenter {
    func onTapAnimalImage(_ url: String) {
        viewState.selectedAnimalImageUrl = url
    }
    
    func onAnimalNameTextChange(_ text: String) {
        viewState.animalName = text
    }
    
    func onTapRegisterButton() {
        viewState.viewKind = .registering
        Task {
            do {
                // チャットの設定リクエスト
                let chatSettingParams = PostChatSettingParameters(animalId: viewState.animalId,
                                                                  animalType: viewState.animalTypeText,
                                                                  animalName: viewState.animalName)
                let chatSettingRequest = RequestPostChatSetting(parameters: chatSettingParams)
                _ = try await APIClient.request(chatSettingRequest)
                
                // Mintリクエスト
                let mintParam = PostCharactersMintParameters(walletAddress: Constants.walletAddress,
                                                              imageUrl: viewState.selectedAnimalImageUrl,
                                                             animalId: viewState.animalId,
                                                              animalType: viewState.animalTypeText,
                                                              animalName: viewState.animalName)
                let mintRequest = RequestPostCharactersMint(parameters: mintParam)
                _ = try await APIClient.request(mintRequest)
                
                UserDefaultsClient.animalId = viewState.animalId
                UserDefaultsClient.animalImageUrl = viewState.selectedAnimalImageUrl
                viewState.viewKind = .complete
            } catch let error {
                print("error occurred:", error)
                viewState.viewKind = .register
            }
        }
    }
}
