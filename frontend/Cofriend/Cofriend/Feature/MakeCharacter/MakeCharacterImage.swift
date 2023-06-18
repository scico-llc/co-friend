//
//  MakeCharacterImage.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import SwiftUI

struct MakeCharacterImage: View {
    @State private var text: String = ""
    
    var body: some View {
        ZStack {
            MakeCharacterImageContent()
        }
    }
}

struct MakeCharacterImageContent: View {
    @State private var text: String = ""
    
    var body: some View {
        VStack {
            Spacer().frame(height: 32)
            VStack {
                Text("キャラクター種類")
                TextField("ネコ", text: $text)
            }.padding(.horizontal, 32)
            Spacer()
            Button(action: {
                print("tapped")
            }, label: {
                Text("作成")
            })
            Spacer().frame(height: 32)
        }
    }
}

struct MakeCharacterImage_Previews: PreviewProvider {
    static var previews: some View {
        MakeCharacterImage()
    }
}
