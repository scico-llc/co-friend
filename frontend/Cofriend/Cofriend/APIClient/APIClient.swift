//
//  APIClient.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/18.
//

import Alamofire

enum APIClient {
    static func request<T: APIRequest>(_ request: T) async throws -> T.ResponseBody {
        let dataRequest = createDataRequest(request)
        return try await validateAndDecode(dataRequest, of: T.ResponseBody.self)
    }
    
    private static func createDataRequest(_ request: some APIRequest) -> DataRequest {
        let urlString = request.baseUrl + request.path
        let headers = HTTPHeaders(request.headers)
        print("url: \(urlString), param: \(String(describing: request.parameters))")
        return AF.request(urlString,
                          method: request.method,
                          parameters: request.parameters,
                          encoder: request.encoder,
                          headers: headers,
                          requestModifier: { $0.timeoutInterval = 120 })
    }
    
    private static func validateAndDecode<T: Decodable>(_ dataRequest: DataRequest, of type: T.Type) async throws -> T {
        try await withCheckedThrowingContinuation { continuation in
            dataRequest
                .validate()
                .responseString { response in
                    print("API response: \(response.debugDescription)")
                }
                .responseDecodable(of: T.self) { response in
                    switch response.result {
                    case let .success(element):
                        continuation.resume(returning: element)
                    case let .failure(error):
                        continuation.resume(throwing: error)
                    }
                }
        }
    }
}
