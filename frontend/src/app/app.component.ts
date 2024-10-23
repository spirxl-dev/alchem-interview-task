import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

interface Event {
  id: number;
  timestamp: string;
  status: string;
  message: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  events: Event[] = [];
  private apiUrl = 'http://localhost:8000/status';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadEvents();
    setInterval(() => this.loadEvents(), 5000);  // Auto-refresh every 5 seconds
  }

  loadEvents(): void {
    this.http.get<Event[]>(this.apiUrl).subscribe(
      data => this.events = data,
      error => console.error('Error loading events', error)
    );
  }
}