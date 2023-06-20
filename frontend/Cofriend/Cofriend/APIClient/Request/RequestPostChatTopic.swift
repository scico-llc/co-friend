//
//  RequestPostChatTopic.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Alamofire

struct RequestPostChatTopic: APIRequest {
    typealias ResponseBody = PostChatTopicResponse
    typealias APIParameters = PostChatTopicParameters
    
    private(set) var method: HTTPMethod = .post
    private(set) var encoder: ParameterEncoder = .json
    private(set) var path: String = "/chat/topic"
    private(set) var parameters: APIParameters
    
    init(parameters: APIParameters) {
        self.parameters = parameters
    }
}

struct PostChatTopicParameters: Encodable {
    let animalId: String
    
    enum CodingKeys: String, CodingKey {
        case animalId = "animal_id"
    }
}

struct PostChatTopicResponse: Decodable {
    let animalId: String
    let message: String
    
    enum CodingKeys: String, CodingKey {
        case animalId = "animal_id"
        case message
    }
}
