//
//  FirestoreClient.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import Foundation
import FirebaseFirestore

final class FirestoreClient {
    static let shared = FirestoreClient()
    private init() {}
    
    let db = Firestore.firestore()
}
