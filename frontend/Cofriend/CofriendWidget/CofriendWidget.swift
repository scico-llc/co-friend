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

    // ユーザーがウィジェットを追加した際に最初に表示されるビュー
    func getSnapshot(in context: Context, completion: @escaping (CofriendWigetEntry) -> ()) {
        Task {
            let entry = try await fetchEntry(date: Date())
            completion(entry)
        }
    }

    // 定期的に更新されるビュー
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
        guard let animalId = UserDefaultsClient.animalId, let imageUrl = UserDefaultsClient.animalImageUrl else {
            return CofriendWigetEntry(date: date, imageUrl: nil, message: "CO-friend アプリを開いてキャラクターを登録しましょう！")
        }
       
        let parameters = PostChatTopicParameters(animalId: animalId)
        let request = RequestPostChatTopic(parameters: parameters)
        do {
            let response = try await APIClient.request(request)
            UserDefaultsClient.cachedMessage = response.message
            return CofriendWigetEntry(date: date, imageUrl: imageUrl, message: response.message)
        } catch {
            // APIからのメッセージ取得が失敗したときはキャッシュしておいたメッセージを表示するようにする
            return CofriendWigetEntry(date: date, imageUrl: imageUrl, message: UserDefaultsClient.cachedMessage ?? "メッセージを取得中...")
        }
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
        .configurationDisplayName("CO-friend widget")
        .description("キャラクターが語りかけてくれるウィジェットです！")
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
