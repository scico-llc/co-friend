//
//  FilledButton.swift
//  Cofriend
//
//  Created by Atsushi Otsubo on 2023/06/20.
//

import SwiftUI

private extension ButtonStyle where Self == FilledButtonStyle {
    static var filled: FilledButtonStyle {
        FilledButtonStyle()
    }
}

private struct FilledButtonStyle: ButtonStyle {
    @Environment(\.isEnabled) var isEnabled
    
    private let enabledColor: Color = .white
    private let disabledColor: Color =  .white
    private let enabledBacgroundColor: Color = .blue
    private let disabledBackgroundColor: Color = .gray
    
    func makeBody(configuration: Configuration) -> some View {
        let backgroundColor = isEnabled ? enabledBacgroundColor : disabledBackgroundColor
        let foregroundColor = isEnabled ? enabledColor : disabledColor
        
        configuration.label
            .frame(minHeight: 48)
            .foregroundColor(foregroundColor)
            .background(backgroundColor)
            .clipShape(Capsule())
            .opacity(configuration.isPressed ? 0.3 : 1.0)
            .animation(.default, value: configuration.isPressed)
    }
}

struct FilledButton: View {
    private let text: String
    private let action: () -> Void
    
    init(
        text: String,
        maxWidth: CGFloat? = .infinity,
        loading: Bool = false,
        action: @escaping () -> Void
    ) {
        self.text = text
        self.action = action
    }
    
    var body: some View {
        Button {
            action()
        } label: {
            let title = SwiftUI.Text(text).bold()
            title
            .font(.headline)
            .padding(.vertical, 24)
            .padding(.horizontal, 24)
            .frame(maxWidth: .infinity)
            .multilineTextAlignment(.center)
        }
        .buttonStyle(.filled)
    }
}

struct FilledButton_Previews: PreviewProvider {
    static var previews: some View {
        VStack {
            FilledButton(
                text: "test", action: { print("tap") }
            )
            FilledButton(
                text: "test", action: { print("tap") }
            )
            .disabled(true)
        }.padding()
    }
}
