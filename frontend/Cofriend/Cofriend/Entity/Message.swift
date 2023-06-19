//
//  Message.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/17.
//

struct Message: Codable, Hashable {
    let role: String
    let content: String
    
    enum CodingKeys: String, CodingKey {
        case role
        case content
    }
}
