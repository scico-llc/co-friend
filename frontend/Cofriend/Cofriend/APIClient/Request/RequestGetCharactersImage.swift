//
//  RequestGetCharactersImage.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import Alamofire

struct RequestGetCharactersImage: APIRequest {
    typealias ResponseBody = GetCharactersImageResponse
    typealias APIParameters = GetCharactersImageParameters
    
    private(set) var method: HTTPMethod = .post
    private(set) var encoder: ParameterEncoder = .json
    private(set) var path: String = "/characters/image"
    private(set) var parameters: APIParameters
    
    init(parameters: APIParameters) {
        self.parameters = parameters
    }
}

struct GetCharactersImageParameters: Encodable {
    let walletAddress: String
    let animalId: String
    let animalType: String
    
    enum CodingKeys: String, CodingKey {
        case walletAddress = "wallet_address"
        case animalId = "animal_id"
        case animalType = "animal_type"
    }
}

struct GetCharactersImageResponse: Decodable {
    let imageUrls: [String]
    
    enum CodingKeys: String, CodingKey {
        case imageUrls = "image_urls"
    }
}
