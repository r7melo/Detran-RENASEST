import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_count_col(path, x_, y_):
    
    df_ = pd.read_csv(path)
    
    sns.barplot(
        data=df_, 
        x=x_, 
        y=y_, 
        palette='Blues_r', 
        hue=y_, 
        legend=False               
    )

def analise_mortos_semana():
    
    tmns = pd.read_csv("./query-results/Tabela Mortos na Semana por Fase do Dia.csv")

    ordem_dias = ['SEGUNDA-FEIRA', 'TERCA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SABADO', 'DOMINGO']
    
    tmns['dia_semana'] = pd.Categorical(tmns['dia_semana'], categories=ordem_dias, ordered=True)
    
    df_plot = tmns.groupby(['dia_semana', 'fase_dia'], observed=False)['total_mortos'].sum().fillna(0).reset_index()
    
    plt.figure(figsize=(14, 6))
    sns.lineplot(
        data=df_plot, 
        x='dia_semana', 
        y='total_mortos', 
        hue='fase_dia', 
        marker='o',      
        linewidth=3,     
        errorbar=None    
    )
    
    plt.title('A Curva do Risco: Evolução Semanal de Óbitos por Turno', fontsize=16, fontweight='bold')
    plt.ylabel('Total de Mortos')
    plt.xlabel('Dia da Semana')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Fase do Dia', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.show()

def analise_mortos_genero():
    tmsg = pd.read_csv("./query-results/Tabela Mortos na Semana por Genero.csv")

    ordem_dias = ['SEGUNDA-FEIRA', 'TERCA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SABADO', 'DOMINGO']
    
    plt.figure(figsize=(12, 6))
    
    sns.lineplot(
        data=tmsg, 
        x='dia_semana', 
        y='total_mortos', 
        hue='genero', 
        marker='o',
        palette=['#3498db', '#e74c3c'],
        linewidth=3
    )
    
    plt.xticks(ticks=range(len(ordem_dias)), labels=ordem_dias, rotation=45)
    plt.title('Evolução Semanal de Óbitos: Masculino vs Feminino', fontsize=14, fontweight='bold')
    plt.ylabel('Total de Mortos')
    plt.xlabel('Dia da Semana')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.show()