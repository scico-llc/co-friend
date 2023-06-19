//
//  RequestGetCharactersImage.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import Alamofire

struct RequestGetCharactersImage: APIRequest {
    // var parameters: [String : String]
    
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
}

struct GetCharactersImageResponse: Decodable {
    let imageUrls: [String]
    
    enum CodingKeys: String, CodingKey {
        case imageUrls = "image_urls"
    }
}
