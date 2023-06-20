//
//  View+Extension.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import SwiftUI

extension View {
    @ViewBuilder func isHidden(_ hidden: Bool) -> some View {
        if hidden {
            self.hidden()
        } else {
            self
        }
    }
}
