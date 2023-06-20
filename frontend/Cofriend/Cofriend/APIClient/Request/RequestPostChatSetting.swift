//
//  RequestPostChatSetting.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Alamofire

struct RequestPostChatSetting: APIRequest {
    typealias ResponseBody = PostChatSettingResponse
    typealias APIParameters = PostChatSettingParameters
    
    private(set) var method: HTTPMethod = .post
    private(set) var encoder: ParameterEncoder = .json
    private(set) var path: String = "/chat/setting"
    private(set) var parameters: APIParameters
    
    init(parameters: APIParameters) {
        self.parameters = parameters
    }
}

struct PostChatSettingParameters: Encodable {
    let animalId: String
    let animalType: String
    let animalName: String
    
    enum CodingKeys: String, CodingKey {
        case animalId = "animal_id"
        case animalType = "animal_type"
        case animalName = "animal_name"
    }
}

struct PostChatSettingResponse: Decodable {}
