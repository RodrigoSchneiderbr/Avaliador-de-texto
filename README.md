<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia de Instalação e Configuração - Avaliador de Redações</title>
    <style>
        :root {
            --primary-color: #2563eb;
            --primary-hover: #1d4ed8;
            --background-color: #f8fafc;
            --card-background: #ffffff;
            --text-color: #1e293b;
            --text-light: #64748b;
            --code-background: #0f172a;
            --code-text: #e2e8f0;
            --border-color: #e2e8f0;
            --success-color: #16a34a;
            --warning-color: #ea580c;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--background-color);
            padding: 40px 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: var(--card-background);
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            border: 1px solid var(--border-color);
        }

        header {
            margin-bottom: 40px;
            text-align: center;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 20px;
        }

        h1 {
            color: #0f172a;
            font-size: 2.2rem;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        p.subtitle {
            color: var(--text-light);
            font-size: 1.1rem;
        }

        h2 {
            color: #1e293b;
            font-size: 1.5rem;
            margin: 30px 0 15px 0;
            padding-left: 10px;
            border-left: 4px solid var(--primary-color);
        }

        h3 {
            color: #334155;
            font-size: 1.1rem;
            margin: 20px 0 10px 0;
        }

        p {
            margin-bottom: 15px;
            color: #334155;
        }

        .step {
            background: #fafafa;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 25px;
        }

        .step-title {
            font-weight: bold;
            font-size: 1.2rem;
            color: #0f172a;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .badge {
            background-color: var(--primary-color);
            color: white;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: normal;
        }

        pre {
            background-color: var(--code-background);
            color: var(--code-text);
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            font-family: "Fira Code", Consolas, Monaco, monospace;
            font-size: 0.9rem;
            margin: 10px 0;
        }

        code {
            font-family: "Fira Code", Consolas, Monaco, monospace;
            background-color: #e2e8f0;
            color: #0f172a;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        pre code {
            background-color: transparent;
            color: inherit;
            padding: 0;
            border-radius: 0;
        }

        ul {
            margin-bottom: 15px;
            padding-left: 20px;
        }

        li {
            margin-bottom: 8px;
        }

        .alert {
            padding: 15px;
            border-radius: 6px;
            margin: 15px 0;
            font-size: 0.95rem;
        }

        .alert-info {
            background-color: #eff6ff;
            border-left: 4px solid var(--primary-color);
            color: #1e40af;
