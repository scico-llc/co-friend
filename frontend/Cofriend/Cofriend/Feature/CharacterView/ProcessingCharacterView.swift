//
//  ProcessingCharacterView.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import SwiftUI

struct ProcessingCharacterView: View {
    let processingMessage: String
    
    init(_ processingMessage: String) {
        self.processingMessage = processingMessage
    }
    
    var body: some View {
        VStack(spacing: 24) {
            Text(processingMessage)
            ProgressView()
        }
        
    }
}

struct ProcessingCharacterView_Previews: PreviewProvider {
    static var previews: some View {
        ProcessingCharacterView("キャラクターを生み出しています...")
    }
}
