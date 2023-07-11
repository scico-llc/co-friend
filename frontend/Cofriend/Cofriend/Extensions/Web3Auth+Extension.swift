//
//  Web3Auth+Extension.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/07/09.
//

import web3
import Web3Auth
import Foundation

extension Web3AuthState: EthereumKeyStorageProtocol {
    public func storePrivateKey(key: Data) throws {
        print("key:", key)
    }
    
    public func loadPrivateKey() throws -> Data {
        guard let privKeyData = self.privKey?.web3.hexData else {
            throw SampleAppError.somethingWentWrong
        }
        return privKeyData
    }
    
}

private enum SampleAppError: Error {
    case noInternetConnection
    case decodingError
    case somethingWentWrong
    case customErr(String)
}

