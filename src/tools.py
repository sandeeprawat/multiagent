"""
Tools and utilities for the multi-agent research system.
"""

import os
import requests
from typing import Optional


def bing_search(query: str, count: int = 5) -> str:
    """
    Perform a Bing web search and return results.
    
    Args:
        query: Search query string
        count: Number of results to return (default: 5)
    
    Returns:
        Formatted string with search results
    """
    api_key = os.getenv("BING_SEARCH_API_KEY")
    endpoint = os.getenv("BING_SEARCH_ENDPOINT", "https://api.bing.microsoft.com/v7.0/search")
    
    if not api_key:
        return "Error: BING_SEARCH_API_KEY not configured"
    
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": count, "mkt": "en-US"}
    
    try:
        response = requests.get(endpoint, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        search_results = response.json()
        
        # Format results
        results = []
        if "webPages" in search_results and "value" in search_results["webPages"]:
            for idx, result in enumerate(search_results["webPages"]["value"], 1):
                results.append(
                    f"{idx}. {result['name']}\n"
                    f"   URL: {result['url']}\n"
                    f"   Snippet: {result.get('snippet', 'N/A')}\n"
                )
        
        return "\n".join(results) if results else "No results found."
    
    except Exception as e:
        return f"Error performing search: {str(e)}"


def save_research_results(results: dict, filename: Optional[str] = None) -> str:
    """
    Save research results to a JSON file.
    
    Args:
        results: Research results dictionary
        filename: Output filename (defaults to timestamped file)
    
    Returns:
        Path to saved file
    """
    import json
    from datetime import datetime
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"research_results_{timestamp}.json"
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    return filename
