// Chat with any Gisoo model through the official OpenAI SDK for Node.js.
//
//   npm install openai
//   GISOO_API_KEY="sk-gisoo-v1-..." node chat.mjs
//
// Docs: https://gisoo.pro/docs/chat
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: process.env.GISOO_BASE_URL ?? "https://gisoo.pro/api/v1",
  apiKey: process.env.GISOO_API_KEY,
});

const response = await client.chat.completions.create({
  model: process.env.GISOO_MODEL ?? "gpt-4o-mini",
  messages: [{ role: "user", content: "سه ایده برای پست اینستاگرام یک گل‌فروشی بده." }],
  max_tokens: 300,
});

console.log(response.choices[0].message.content);
