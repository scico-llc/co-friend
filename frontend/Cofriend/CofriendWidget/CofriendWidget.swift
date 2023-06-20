//
//  CofriendWidget.swift
//  CofriendWidget
//
//  Created by Atsushi Otsubo on 2023/06/11.
//

import WidgetKit
import SwiftUI
import Alamofire

struct CofriendWigetEntry: TimelineEntry {
    let date: Date
    let imageUrl: String?
    let message: String
}

struct Provider: TimelineProvider {
    func placeholder(in context: Context) -> CofriendWigetEntry {
        CofriendWigetEntry(date: Date(), imageUrl: nil, message: "Placeholder")
    }

    // プレビュー/ギャラリーに表示されるビュー、ユーザーがウィジェットを追加した際に最初に表示されるビュー
    func getSnapshot(in context: Context, completion: @escaping (CofriendWigetEntry) -> ()) {
        Task {
            let entry = try await fetchEntry(date: Date())
            completion(entry)
        }
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> ()) {
        Task {
            let currentDate = Date()
            let entryDate = Calendar.current.date(byAdding: .minute, value: 15, to: currentDate)!
            let entry = try await fetchEntry(date: entryDate)
            let timeline = Timeline(entries: [entry], policy: .atEnd)
            completion(timeline)
        }
    }
    
    private func fetchEntry(date: Date) async throws -> CofriendWigetEntry {
        let animalId = UserDefaultsClient.animalId ?? "xxxxxxxxxxxx123"
        let imageUrl = UserDefaultsClient.animalImageUrl ?? "https://storage.googleapis.com/co-friend-dev.appspot.com/1234/0.png"
       
        let parameters = PostChatTopicParameters(animalId: animalId)
        let request = RequestPostChatTopic(parameters: parameters)
        print("request.path: ", request.path)
        let response = try await APIClient.request(request)
        print("response: ", response.message)
        // Mock:
//        let response = PostChatTopicResponse(animalId: animalId, message: "こんにちはこんにちはこんにちはこんにちはこんにちはこんにちは")
        
        return CofriendWigetEntry(date: date, imageUrl: imageUrl, message: response.message)
    }
}

struct CofriendWidgetEntryView : View {
    @Environment(\.widgetFamily) var family: WidgetFamily
    var entry: Provider.Entry

    @ViewBuilder
    var body: some View {
        switch family {
        case .systemMedium: WidgetMediumView(imageUrl: entry.imageUrl, message: entry.message)
        default: Text("medium のみ対応しています")
        }
    }
}

struct WidgetMediumView: View {
    let imageUrl: String?
    let message: String
    
    var body: some View {
        HStack (spacing: 12) {
            if let url = URL(string: imageUrl ?? ""),
               let imageData = try? Data(contentsOf: url),
               let uiImage = UIImage(data: imageData) {
                Image(uiImage: uiImage)
                    .resizable()
                    .frame(width: 120, height: 120)
            } else {
                ProgressView()
                    .frame(width: 120, height: 120)
            }
            
            Text(message)
                .frame(maxWidth: .infinity)
                .multilineTextAlignment(.leading)
                .padding(.trailing, 16)
        }
    }
}

struct CofriendWidget: Widget {
    let kind: String = "CofriendWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: Provider()) { entry in
            CofriendWidgetEntryView(entry: entry)
        }
        .configurationDisplayName("My Widget")
        .description("This is an example widget.")
    }
}

struct CofriendWidget_Previews: PreviewProvider {
    static var previews: some View {
        let entry = Provider.Entry(date: Date(), imageUrl: "https://storage.googleapis.com/co-friend-dev.appspot.com/1234/2.png",
                                   message: "こんにちはこんにちはこんにちはこんにちはこんにちは")
        CofriendWidgetEntryView(entry: entry)
            .previewContext(WidgetPreviewContext(family: .systemMedium))
    }
}
