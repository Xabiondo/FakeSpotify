import { ComponentFixture, TestBed } from '@angular/core/testing';
import { CancionComponent } from './cancion.component';



describe('Cancion', () => {
  let component: CancionComponent;
  let fixture: ComponentFixture<CancionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CancionComponent]
    })
      .compileComponents();

    fixture = TestBed.createComponent(CancionComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
