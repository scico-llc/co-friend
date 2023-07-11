//
//  LoginView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import SwiftUI

struct LoginView: View {
    @ObservedObject private(set) var presenter = Presenter()
    
    var body: some View {
        NavigationStack {
            VStack(alignment: .center, spacing: 0) {
                Spacer().frame(height: 128)
                Image("co-friend-icon")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(maxWidth: .infinity)
                    .padding(.horizontal, 32)
                Spacer()
                FilledButton(text: "サインアップ") {
                    presenter.onTapLoginButton()
                }.padding(.horizontal, 32)
                    .padding(.bottom, 64)
            }
            .onAppear {
                presenter.onAppeare()
            }
            .navigationDestination(isPresented: $presenter.viewState.isLoggedIn) {
                ChatView()
            }
        }
    }
}

struct LoginView_Previews: PreviewProvider {
    static var previews: some View {
        LoginView()
    }
}
