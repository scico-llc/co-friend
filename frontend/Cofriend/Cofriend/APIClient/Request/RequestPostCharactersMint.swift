//
//  RequestPostCharactersMint.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Alamofire

struct RequestPostCharactersMint: APIRequest {
    typealias ResponseBody = PostCharactersMintResponse
    typealias APIParameters = PostCharactersMintParameters
    
    private(set) var method: HTTPMethod = .post
    private(set) var encoder: ParameterEncoder = .json
    private(set) var path: String = "/characters/mint"
    private(set) var parameters: APIParameters
    
    init(parameters: APIParameters) {
        self.parameters = parameters
    }
}

struct PostCharactersMintParameters: Encodable {
    let walletAddress: String
    let imageUrl: String
    let animalId: String
    let animalType: String
    let animalName: String
    
    enum CodingKeys: String, CodingKey {
        case walletAddress = "wallet_address"
        case imageUrl = "image_url"
        case animalId = "animal_id"
        case animalType = "animal_type"
        case animalName = "animal_name"
    }
}

struct PostCharactersMintResponse: Decodable {}
