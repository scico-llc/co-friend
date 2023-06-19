//
//  APIRequest.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import Alamofire

protocol APIRequest {
    associatedtype ResponseBody: Decodable
    associatedtype APIParameters: Encodable
    
    var baseUrl: String { get }
    var headers: [String: String] { get }
    var method: HTTPMethod { get }
    var encoder: ParameterEncoder { get }
    var path: String { get }
    var parameters: APIParameters { get }
}

extension APIRequest {
    var baseUrl: String { Constants.baseUrl }
    var headers: [String: String] { ["Authorization": "Bearer \(Constants.token)"] }
}
