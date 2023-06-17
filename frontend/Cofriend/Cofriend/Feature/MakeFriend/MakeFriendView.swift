//
//  MakeFriendView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/17.
//

import SwiftUI

struct MakeFriendView: View {
    @State private var name = ""
    @State private var input1 = ""
    @State private var input2 = ""
    
    var body: some View {
        VStack(alignment: .center, spacing: 12) {
            Spacer().frame(height: 32)
            VStack(alignment: .leading) {
                Text("Friend Name")
                    .font(.subheadline)
                TextField("Input friend name",
                            text: $name)
                    .textFieldStyle(.roundedBorder)
                    .padding(.bottom, 12)

                Text("title1")
                    .font(.subheadline)
                TextField("Input friend name",
                            text: $input1)
                    .textFieldStyle(.roundedBorder)
                    .padding(.bottom, 12)

                Text("title2")
                    .font(.subheadline)
                TextField("Input friend name",
                            text: $input2)
                    .textFieldStyle(.roundedBorder)
                    .padding(.bottom, 12)
            }
            Spacer()
            Button(action: {
                print("tapped")
            }, label: {
                Text("キャラクター作成")
            })
            Spacer().frame(height: 32)
        }
        .padding(.horizontal, 24)
    }
}

struct MakeFriendView_Previews: PreviewProvider {
    static var previews: some View {
        MakeFriendView()
    }
}
