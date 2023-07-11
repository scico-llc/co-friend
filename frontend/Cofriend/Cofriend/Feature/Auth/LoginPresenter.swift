//
//  LoginPresenter.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Foundation
import Web3Auth
import web3

extension LoginView {
    @MainActor struct ViewState {
        var isLoggedIn: Bool = false
    }
    
    @MainActor final class Presenter: ObservableObject {
         @Published var viewState = ViewState()
        
        func onAppeare() {
            // ここをコメントアウトすると、walletAddressの有無でログイン判定できる (毎回認証が走るのをスキップできる)
            // viewState.isLoggedIn = UserDefaultsClient.walletAddress == nil ? false : true
        }
        
        func onTapLoginButton() {
            login(provider: .GOOGLE)
        }
        
        private func login(provider: Web3AuthProvider) {
            Task {
                do {
                    let user = try await Web3Auth(W3AInitParams(
                        clientId: Constants.clientId,
                        network: .testnet
                    ))
                        .login(W3ALoginParams(loginProvider: provider))
                    let account = try EthereumAccount(keyStorage: user)
                    UserDefaultsClient.walletAddress = account.address.value
                    viewState.isLoggedIn = true
                } catch {
                    print("Error")
                }
            }
        }
    }
}

