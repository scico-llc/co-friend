//
//  Chat.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Foundation

struct Chat: Codable, Identifiable {
    let id: String
    let history: [Message]
    let name: String
    let type: String
    
    enum CodingKeys: String, CodingKey {
        case id
        case history
        case name
        case type
    }
}
