//
//  UserDefaultsClient.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/19.
//

import Foundation

struct UserDefaultsClient {
    private static let userDefaults = UserDefaults(suiteName: "group.group.co-friend.Cofriend.WidgetExtension")
    
    enum StringItem: String {
        case walletAddress
        case animalId
        case animalImageUrl
        /// Widgetでのメッセージ取得が失敗した時用に最新のメッセージをキャッシュしておく
        case cachedMessage
    }
    
    private static func set(value: String, forKey item: StringItem) {
        userDefaults?.set(value, forKey: item.rawValue)
    }
    
    private static func string(forKey item: StringItem) -> String? {
        userDefaults?.string(forKey: item.rawValue)
    }
}

extension UserDefaultsClient {
    static var walletAddress: String? {
        get {
            return string(forKey: .walletAddress)
        }
        set {
            set(value: newValue!, forKey: .walletAddress)
        }
    }
    
    static var animalId: String? {
        get {
            return string(forKey: .animalId)
        }
        set {
            set(value: newValue!, forKey: .animalId)
        }
    }
    
    static var animalImageUrl: String? {
        get {
            return string(forKey: .animalImageUrl)
        }
        set {
            set(value: newValue!, forKey: .animalImageUrl)
        }
    }
    
    static var cachedMessage: String? {
        get {
            return string(forKey: .cachedMessage)
        }
        set {
            set(value: newValue!, forKey: .cachedMessage)
        }
    }

}
