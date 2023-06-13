//
//  CofriendWidget.swift
//  CofriendWidget
//
//  Created by Atsushi Otsubo on 2023/06/11.
//

import WidgetKit
import SwiftUI

struct Provider: TimelineProvider {
    func placeholder(in context: Context) -> SimpleEntry {
        SimpleEntry(date: Date(), text: "", imageName: "leaf")
    }

    func getSnapshot(in context: Context, completion: @escaping (SimpleEntry) -> ()) {
        let entry = SimpleEntry(date: Date(), text: "", imageName: "leaf")
        completion(entry)
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> ()) {
        var entries: [SimpleEntry] = []

        // Generate a timeline consisting of five entries an hour apart, starting from the current date.
        let currentDate = Date()
        for hourOffset in 0 ..< 5 {
            let entryDate = Calendar.current.date(byAdding: .hour, value: hourOffset, to: currentDate)!
            let entry = SimpleEntry(date: entryDate, text: "hourOffset: \(hourOffset)", imageName: "leaf")
            entries.append(entry)
        }

        let timeline = Timeline(entries: entries, policy: .atEnd)
        completion(timeline)
    }
}

struct SimpleEntry: TimelineEntry {
    let date: Date
    let text: String
    let imageName: String
}

struct CofriendWidgetEntryView : View {
    var entry: Provider.Entry

    var body: some View {
        HStack {
            Image(entry.imageName)
                .frame(maxWidth: 100, maxHeight: 100)
            Text(entry.date, style: .time)
            Text("text: \(entry.text)")
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
        CofriendWidgetEntryView(entry: SimpleEntry(date: Date(), text: "test", imageName: "leaf"))
            .previewContext(WidgetPreviewContext(family: .systemSmall))
    }
}
