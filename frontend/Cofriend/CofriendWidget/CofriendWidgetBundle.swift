//
//  CofriendWidgetBundle.swift
//  CofriendWidget
//
//  Created by Atsushi Otsubo on 2023/06/11.
//

import WidgetKit
import SwiftUI

@main
struct CofriendWidgetBundle: WidgetBundle {
    var body: some Widget {
        CofriendWidget()
        CofriendWidgetLiveActivity()
    }
}
