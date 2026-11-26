import pandas as pd
import io
def read_file(file_path: str = None, content: bytes = None, filename: str = '') -> tuple[str, dict]:
    try:
        if content:
            if filename.endswith('.csv'):
                df = pd.read_csv(io.BytesIO(content))
            elif filename.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(io.BytesIO(content))
            else:
                return content.decode('utf-8', errors='ignore'), {'rows': 0, 'columns': 0, 'column_names': [], 'sample': '', 'data_type': 'text'}
        else:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                return text, {'rows': 0, 'columns': 0, 'column_names': [], 'sample': text[:500], 'data_type': 'text'}
        info = {
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': list(df.columns),
            'sample': df.head(5).to_string(),
            'data_type': 'table'
        }
        return df.to_string(), info
    except Exception as e:
        return f'Error reading file: {e}', {}
