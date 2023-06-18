//
//  TopView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/17.
//

import SwiftUI

struct TopView: View {
    var body: some View {
        NavigationView {
            VStack {
                NavigationLink(destination: RegisterCharacterView()) {
                    Text("友達を作る")
                        .frame(minWidth: 250, minHeight: 50)
                }
                
                NavigationLink(destination: ChatView()) {
                    Text("会話する")
                        .frame(minWidth: 250, minHeight: 50)
                }
            }
        }
    }
}

struct TopView_Previews: PreviewProvider {
    static var previews: some View {
        TopView()
    }
}
