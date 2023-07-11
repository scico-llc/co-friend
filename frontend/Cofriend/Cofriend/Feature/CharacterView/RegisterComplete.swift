//
//  RegisterComplete.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import SwiftUI

struct RegisterCompleteView: View {
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        Text("キャラクターの登録が完了しました")
        FilledButton(text: "閉じる", action: {
            dismiss()
        })
        .padding(.horizontal, 20)
    }
}
