def resolve_context(current_query: str, history: list[str]) -> str:
    """
    Simulates a context resolver that extracts relevant information from past interactions.
    In a real system, this would involve advanced NLP, database lookups, CRM data, etc.
    For this example, we use simple keyword matching.
    """
    context_elements = []

    # --- This section simulates the 'context resolver' logic ---
    # It tries to identify key entities or past intents from the history.
    if any("Ürün A" in msg for msg in history):
        context_elements.append("Müşteri daha önce Ürün A ile ilgilenmişti.")
    if any("Ürün B" in msg for msg in history):
        context_elements.append("Müşteri daha önce Ürün B hakkında endişe dile getirmişti.")
    if any("satın alma" in msg or "ödeme" in msg for msg in history):
        context_elements.append("Müşterinin geçmişte satın alma veya ödeme ile ilgili soruları olmuştu.")

    # Combine extracted elements into a single context string
    if context_elements:
        return "Geçmiş Etkileşim Özeti: " + " ".join(context_elements) + " "
    return ""

# --- Simulation Setup ---

# Simulate a customer's past interactions (e.g., from CRM, chat logs, emails)
customer_history = [
    "Geçen hafta Ürün A hakkında bir soru sormuştum.",
    "Dün Ürün B'nin garanti koşulları hakkında endişelerimi dile getirmiştim.",
    "Ürün A'nın özelliklerini tekrar incelemek istiyorum."
]

# Simulate the current customer query received by the AI agent
current_query = "Ürün A'yı şimdi satın almak istiyorum. Ödeme seçenekleri nelerdir?"

print("--- Yapay Zeka Satış Temsilcisi İçin Bağlam Çözücü Simülasyonu ---")
print(f"\nMüşteri Geçmişi:\n{'-'*30}")
for i, msg in enumerate(customer_history):
    print(f"  {i+1}. {msg}")
print(f"{'-'*30}\n")

print(f"Mevcut Müşteri Sorgusu: {current_query}\n")

# --- Scenario 1: AI Agent without Context Resolver ---
# The AI only receives the current message, lacking historical context.
print("1. Bağlam Çözücü OLMADAN Yapay Zeka Girişi:")
# This illustrates the problem: AI only gets the current query, potentially missing crucial background.
ai_input_without_context = current_query
print(f"  AI'ya gönderilen mesaj: '{ai_input_without_context}'")
print("  (AI, müşterinin Ürün A ile geçmiş ilgisini veya Ürün B endişesini doğrudan bilmeyebilir.)\n")

# --- Scenario 2: AI Agent WITH Context Resolver ---
# The context resolver processes history and current query to create an enriched context.
print("2. Bağlam Çözücü İLE Yapay Zeka Girişi:")
# This part demonstrates the core concept: the context resolver generating a summary.
resolved_context = resolve_context(current_query, customer_history)

# The AI receives the enriched context along with the current query.
ai_input_with_context = resolved_context + current_query
print(f"  Çözümlenmiş Bağlam: '{resolved_context.strip()}'")
print(f"  AI'ya gönderilen mesaj: '{ai_input_with_context}'")
print("  (AI, müşterinin geçmişteki Ürün A ilgisini ve Ürün B endişesini bilerek daha iyi ve ilgili yanıt verebilir.)\n")

print("--- Simülasyon Sonu ---")
