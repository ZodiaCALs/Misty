// swift-tools-version: 5.9
// SPDX-FileCopyrightText: 2026 ZodiaCALs
// SPDX-License-Identifier: Apache-2.0
import PackageDescription

let package = Package(
    name: "MistyTokens",
    platforms: [.iOS(.v15), .macOS(.v12), .tvOS(.v15), .watchOS(.v8), .visionOS(.v1)],
    products: [.library(name: "MistyTokens", targets: ["MistyTokens"])],
    targets: [.target(name: "MistyTokens")]
)
