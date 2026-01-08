import matplotlib.pyplot as plt
import seaborn as sns

def plot_counts(df, coluna, titulo=None, palette='viridis'):
    """
    Gera um gráfico de barras simples para contagem de valores de uma coluna.
    """
    plt.figure(figsize=(12, 6))
    
    # 1. Preparar os dados
    df_plot = df[coluna].value_counts().reset_index()
    df_plot.columns = [coluna, 'contagem']
    
    # 2. Criar o plot (sem os avisos de palette/hue)
    ax = sns.barplot(
        data=df_plot, 
        x=coluna, 
        y='contagem', 
        hue=coluna, 
        palette=palette, 
        legend=False
    )
    
    # 3. Estética do gráfico
    if titulo:
        plt.title(titulo, fontsize=16, fontweight='bold', pad=15)
    else:
        plt.title(f'Distribuição por {coluna.replace("_", " ").title()}', fontsize=14)
        
    plt.xticks(rotation=45)
    plt.xlabel('')
    plt.ylabel('Quantidade')
    
    # Adiciona os números em cima das barras para facilitar a leitura
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,d}'.replace(',', '.'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points',
                    fontsize=10, fontweight='bold')

    sns.despine() # Remove as bordas desnecessárias
    plt.tight_layout()
    plt.show()