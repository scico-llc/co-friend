//
//  UserDefaultsClient.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/19.
//

import Foundation

enum UserDefaultsClient {
    enum StringItem: String {
        case animalId
        case animalImageUrl
    }
    
    private static func set(value: String, forKey item: StringItem) {
        UserDefaults.standard.set(value, forKey: item.rawValue)
    }
    
    private static func string(forKey item: StringItem) -> String? {
        UserDefaults.standard.string(forKey: item.rawValue)
    }
}

extension UserDefaultsClient {
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
}
