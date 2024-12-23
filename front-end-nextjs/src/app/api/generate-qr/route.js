import { NextResponse } from "next/server";
import axios from "axios";

const API_URL = 'http://ae0b8dc5ea6814758a787ae3071683df-1171805389.us-east-1.elb.amazonaws.com';

export async function POST(request) {
    const { searchParams } = new URL(request.url);
    const url = searchParams.get("url");

    if (!url) {
        return NextResponse.json({ error: "URL is required" }, { status: 400 });
    }

    try {
        const response = await axios.post(`${API_URL}/generate-qr/?url=${encodeURIComponent(url)}`);
        return NextResponse.json(response.data);
    } catch (error) {
        console.error("Error generating QR Code:", error);
        return NextResponse.json({ error: "Error generating QR Code" }, { status: 500 });
    }
}