//
//  RequestPostChat.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Alamofire

struct RequestPostChat: APIRequest {
    typealias ResponseBody = PostChatResponse
    typealias APIParameters = PostChatParameters
    
    private(set) var method: HTTPMethod = .post
    private(set) var encoder: ParameterEncoder = .json
    private(set) var path: String = "/chat"
    private(set) var parameters: APIParameters
    
    init(parameters: APIParameters) {
        self.parameters = parameters
    }
}

struct PostChatParameters: Encodable {
    let animalId: String
    let message: String
    
    enum CodingKeys: String, CodingKey {
        case animalId = "animal_id"
        case message
    }
}

struct PostChatResponse: Decodable {
    let animalId: String
    let message: String
    
    enum CodingKeys: String, CodingKey {
        case animalId = "animal_id"
        case message
    }
}
