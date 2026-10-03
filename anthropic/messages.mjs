// Claude through Gisoo with the official Anthropic SDK for Node.js.
//
//   npm install @anthropic-ai/sdk
//   GISOO_API_KEY="sk-gisoo-v1-..." node messages.mjs
//
// Docs: https://gisoo.pro/docs/anthropic
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://gisoo.pro/api", // not .../v1: the SDK adds /v1/messages itself
  apiKey: process.env.GISOO_API_KEY,
});

const message = await client.messages.create({
  model: "claude-sonnet-5-5",
  max_tokens: 400,
  messages: [{ role: "user", content: "سه ایدهٔ اسم برای یک کافه کتاب پیشنهاد بده." }],
});

console.log(message.content[0].text);
